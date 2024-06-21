package com.example.job_com.data.network

object APIClient {
    private const val BASE_URL = "https://my_server"

    val instance: Retrofit by lazy {
        Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
    }
}