from rest_framework import serializers

from blango_auth.models import User
from blog.models import Post, Tag, Comment


# Remember that get_or_create() will fetch an instance from the database given the search parameters, or create one if
# it doesn't exists. It returns a 2-element tuple (object, created), where object is the Tag (which might have just been
# created) and created is True if the object was created or False if not. We just want the object so we return the first
# element from the tuple.
# The fail() method is just a shortcut method that DRF provides, to raise a ValidationError.
# The get_or_create method returns a tuple with two items. The first item (‘0’) is the tag for the post. The second item
# (‘1’) is a boolean value that represents if the method created the tag or not. So changing 0 to 1 replaces the string
# value of the tag with a boolean value.


class TagField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(value=data.lower())[0]
        except (TypeError, ValueError):
            self.fail(f"Tag value {data} is invalid")


class PostSerializer(serializers.ModelSerializer):
    # tags = serializers.SlugRelatedField(
    #     slug_field="value", many=True, queryset=Tag.objects.all()
    # )
    tags = TagField(
        slug_field="value", many=True, queryset=Tag.objects.all()
    )

    author = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(), view_name="api_user_detail", lookup_field="email"
    )

    class Meta:
        model = Post
        fields = "__all__"
        readonly = ["modified_at", "created_at"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "creator", "content", "modified_at", "created_at"]
        readonly = ["modified_at", "created_at"]


class PostDetailSerializer(PostSerializer):
    comments = CommentSerializer(many=True)

    def update(self, instance, validated_data):
        comments = validated_data.pop("comments")

        instance = super(PostDetailSerializer, self).update(instance, validated_data)

        for comment_data in comments:
            if comment_data.get("id"):
                # comment has an ID so was pre-existing
                continue
            comment = Comment(**comment_data)
            comment.creator = self.context["request"].user
            comment.content_object = instance
            comment.save()

        return instance
