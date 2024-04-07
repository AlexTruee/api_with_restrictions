from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
         Проверка прав на конкретный объект

         """
        if request.method == 'GET':
            return True
        return request.user == obj.creator
