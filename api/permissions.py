from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):  
        def has_object_permission(self, request, view, obj):
                return bool(request.method == "GET" or 
                        obj.author == request.user or 
                        request.user.is_staff or 
                        request.user.is_superuser)