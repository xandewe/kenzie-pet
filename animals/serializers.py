from rest_framework import serializers
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer
from .models import Animal
from groups.models import Group
from traits.models import Trait
from django.core.exceptions import ValidationError


class AnimalSerializer(serializers.Serializer):
    INVALID_UPDATE = {"traits", "group", "sex"}
    
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.CharField()
    group = GroupSerializer()
    traits = TraitSerializer(many=True)
    age_in_human_years = serializers.SerializerMethodField()

    def create(self, validated_data: dict):
        group = validated_data.pop("group")
        traits = validated_data.pop("traits")

        get_group, _ = Group.objects.get_or_create(**group)
        animal: Animal = Animal(**validated_data, group=get_group)
        animal.save()

        for trait in traits:
            get_trait, _ = Trait.objects.get_or_create(**trait)
            animal.traits.add(get_trait)


        return animal

    def update(self, instance, validated_data: dict):
        invalid_update = self.INVALID_UPDATE.intersection(set(validated_data))

        if invalid_update:
            res = {key: f"You can not update {key} property." for key in invalid_update}
            raise ValidationError(res)
        
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        
        return instance

    def get_age_in_human_years(self, obj: Animal):
        return obj.convert_in_human_years()
