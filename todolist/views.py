# filepath: /Users/angelgracemurillo/AppDev-API/appdevapi/todolist/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ToDoList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Example response for the ToDo list
        return Response({"todos": ["Task 1", "Task 2", "Task 3"]})

class ToDoDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, todo_id):
        # Example response for a specific ToDo item
        return Response({"todo": f"Details of Task {todo_id}"})

class SecureHelloView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello, {request.user.username}!"})