package com.example.job_com.data.repo

class UserRepo (private val apiService: APIService){

    suspend fun authenticate(email: String, password: String): AuthResponse {
        val request = AuthRequest(email, password)
        return apiService.authenticate(request)
    }

    suspend fun register(name: String, email: String, password: String): RegistrationResponse {
        val request = RegistrationRequest(name, email, password)
        return apiService.register(request)
    }
}