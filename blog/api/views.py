from rest_framework import generics, viewsets
from rest_framework.throttling import ScopedRateThrottle
from blango_auth.models import User
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject
from blog.api.serializers import PostSerializer, UserSerializer, PostDetailSerializer, TagSerializer, CommentSerializer
from blog.models import Post, Comment
from blog.models import Tag
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers, vary_on_cookie

from rest_framework.exceptions import PermissionDenied


from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


# class PostViewSet(viewsets.ModelViewSet):
#     # existing attributes omitted
#
#     @action(methods=["get"], detail=False, name="Posts by the logged in user")
#     def mine(self, request):
#         if request.user.is_anonymous:
#             raise PermissionDenied("You must be logged in to see which Posts are yours")
#         posts = self.get_queryset().filter(author=request.user)
#         serializer = PostSerializer(posts, many=True, context={"request": request})
#         return Response(serializer.data)

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers, vary_on_cookie


# class PostViewSet(viewsets.ModelViewSet):
#     permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
#     queryset = Post.objects.all()
#
#     def get_serializer_class(self):
#         if self.action in ("list", "create"):
#             return PostSerializer
#         return PostDetailSerializer
#
# @method_decorator(cache_page(120))
# def list(self, *args, **kwargs):
    # return super(PostViewSet, self).list(*args, **kwargs)
#     @method_decorator(cache_page(300))
#     @method_decorator(vary_on_headers("Authorization"))
#     @method_decorator(vary_on_cookie)
#     @action(methods=["get"], detail=False, name="Posts by the logged in user")
#     def mine(self, request):
#         if request.user.is_anonymous:
#             raise PermissionDenied("You must be logged in to see which Posts are yours")
#         posts = self.get_queryset().filter(author=request.user)
#         serializer = PostSerializer(posts, many=True, context={"request": request})
#         return Response(serializer.data)

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "post_api"

    # def get_queryset(self):
    #     if self.request.user.is_anonymous:
    #         # published only
    #         return self.queryset.filter(published_at__lte=timezone.now())
    #
    #     if self.request.user.is_staff:
    #         # allow all
    #         return self.queryset
    #
    #     # filter for own or
    #     return self.queryset.filter(
    #         Q(published_at__lte=timezone.now()) | Q(author=self.request.user)
    #     )
    # def get_queryset(self):
    #     # queryset has been set by applying user filtering rules
    #
    #     # fetch the period_name URL parameter from self.kwargs
    #     time_period_name = self.kwargs.get("period_name")
    #
    #     if not time_period_name:
    #         # no further filtering required
    #         return queryset
    #
    #     if time_period_name == "new":
    #         return queryset.filter(published_at__gte=timezone.now() - timedelta(hours=1))
    #     elif time_period_name == "today":
    #         return queryset.filter(
    #             published_at__date=timezone.now().date(),
    #         )
    #     elif time_period_name == "week":
    #         return queryset.filter(published_at__gte=timezone.now() - timedelta(days=7))
    #     else:
    #         raise Http404(
    #             f"Time period {time_period_name} is not valid, should be "
    #             f"'new', 'today' or 'week'"
    #         )
    # def get_queryset(self):
    #     if self.request.user.is_anonymous:
    #         # published only
    #         queryset = self.queryset.filter(published_at__lte=timezone.now())
    #
    #     elif not self.request.user.is_staff:
    #         # allow all
    #         queryset = self.queryset
    #     else:
    #         queryset = self.queryset.filter(
    #             Q(published_at__lte=timezone.now()) | Q(author=self.request.user)
    #         )
    #
    #     time_period_name = self.kwargs.get("period_name")
    #
    #     if not time_period_name:
    #         # no further filtering required
    #         return queryset
    #
    #     if time_period_name == "new":
    #         return queryset.filter(
    #             published_at__gte=timezone.now() - timedelta(hours=1)
    #         )
    #     elif time_period_name == "today":
    #         return queryset.filter(
    #             published_at__date=timezone.now().date(),
    #         )
    #     elif time_period_name == "week":
    #         return queryset.filter(published_at__gte=timezone.now() - timedelta(days=7))
    #     else:
    #         raise Http404(
    #             f"Time period {time_period_name} is not valid, should be "
    #             f"'new', 'today' or 'week'"
    #         )


class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "user_api"
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
