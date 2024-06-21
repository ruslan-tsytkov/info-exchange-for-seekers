package com.example.job_com.data.network.request

data class CreatePostRequest(
    val userId: Int,
    val title: String,
    val content: String
)