import axios from 'axios'

const API = axios.create({
	// baseURL: import.meta.env.REACT_APP_BASEURL,
	baseURL: 'http://localhost:8080/',
})
export default API
