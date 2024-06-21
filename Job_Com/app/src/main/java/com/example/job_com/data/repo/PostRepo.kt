package com.example.job_com.data.repo

class PostRepo(private val apiService: APIService) {

    suspend fun getPosts(userId: Int): List<Post> {
        return apiService.getPosts(GetPostsRequest(userId))
    }

    suspend fun createPost(userId: Int, title: String, content: String): CreatePostResponse {
        val request = CreatePostRequest(userId, title, content)
        return apiService.createPost(request)
    }
}