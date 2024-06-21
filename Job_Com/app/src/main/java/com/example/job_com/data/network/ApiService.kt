package com.example.job_com.data.network

interface APIService {

    @POST("auth/login")
    suspend fun authenticate(@Body request: AuthRequest): AuthResponse

    @POST("auth/register")
    suspend fun register(@Body request: RegistrationRequest): RegistrationResponse

    @POST("posts")
    suspend fun getPosts(@Body request: GetPostsRequest): GetPostsResponse

    @POST("posts/create")
    suspend fun createPost(@Body request: CreatePostRequest): CreatePostResponse

    companion object {
        val api: APIService by lazy {
            APIClient.instance.create(APIService::class.java)
        }
    }
}
