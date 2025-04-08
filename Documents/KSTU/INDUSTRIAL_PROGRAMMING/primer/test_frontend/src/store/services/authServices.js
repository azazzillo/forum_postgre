import API from './api'

export const loginUser = async (email, password) => {
	const response = await API.post("auth/login", {
        email: email,
        password: password
    });
	return response.data
}
