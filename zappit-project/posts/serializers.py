from rest_framework import serializers
from .models import Post
from .models import Vote


class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'poster', 'poster_id', 'created_at', 'votes']

    def get_votes(self, post): # precisa necessariamente ser get_<nome do campo com SerializerMethodField>
        return Vote.objects.filter(post=post).count()
    
    
    
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']