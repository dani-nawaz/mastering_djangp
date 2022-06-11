from rest_framework import serializers

from drones.models import DroneCategory, Drone, Competition, Pilot


class DroneCategorySerializer(serializers.ModelSerializer):
    drones = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = DroneCategory
        fields = (
            'pk',
            'name',
            'drones')


class DroneSerializer(serializers.ModelSerializer):
    # Display the category name
    drone_category = serializers.SlugRelatedField(queryset=DroneCategory.objects.all(), slug_field='name')

    class Meta:
        model = Drone
        fields = (
            'name',
            'drone_category',
            'manufacturing_date',
            'has_it_competed',
            'inserted_timestamp')


class DroneMiniSerializer(serializers.ModelSerializer):
    # Display the category name
    drone_category = serializers.SlugRelatedField(queryset=DroneCategory.objects.all(), slug_field='name')

    class Meta:
        model = Drone
        fields = (
            'name',
            'drone_category',
        )


class CompetitionSerializer(serializers.ModelSerializer):
    # Display all the details for the related drone
    drone = DroneMiniSerializer()

    class Meta:
        model = Competition
        fields = (
            'pk',
            'distance_in_feet',
            'distance_achievement_date',
            'drone')


#
#
class PilotSerializer(serializers.ModelSerializer):
    competitions = CompetitionSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(
        choices=Pilot.GENDER_CHOICES)
    gender_description = serializers.CharField(
        source='get_gender_display',
        read_only=True)
    noice = serializers.CharField(
        source='get_gender_display',
        read_only=True)

    class Meta:
        model = Pilot
        fields = (
            'name',
            'gender',
            "noice",
            'gender_description',
            'races_count',
            'inserted_timestamp',
            'competitions')


#
class PilotCompetitionSerializer(serializers.ModelSerializer):
    # Display the pilot's name
    pilot = serializers.SlugRelatedField(queryset=Pilot.objects.all(), slug_field='name')
    # Display the drone's name
    drone = serializers.SlugRelatedField(queryset=Drone.objects.all(), slug_field='name')

    class Meta:
        model = Competition
        fields = (
            'pk',
            'distance_in_feet',
            'distance_achievement_date',
            'pilot',
            'drone')
