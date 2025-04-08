import { useNavigate, useLocation } from "react-router-dom";
import { useDispatch, useSelector } from 'react-redux';
import React, { useState, useEffect } from "react";
import axios from "axios";
import { login } from "../store/slices/authSlice"

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [localError, setLocalError] = useState(null);
  
  const dispatch = useDispatch()
  const navigate = useNavigate();
  const location = useLocation();
  
  const successMessage = location.state?.successMessage;
  const authError = useSelector(state => state.auth.error); // <- от Redux

  useEffect(() => {
    const token = localStorage.getItem("accessToken");
    var qwe = authError;
    debugger
    if (token) {
      navigate("/profile");
    }
  }, [navigate]);

  const handleSubmit = async (event) => {
    debugger
    event.preventDefault();
    setLocalError(null); // сбрасываем локальную ошибку

    const result = await dispatch(login({ email, password }));
    if (login.fulfilled.match(result)) {
      navigate("/profile");
    } else {
      setLocalError(result.payload);
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="w-full max-w-md bg-white rounded-2xl shadow-lg p-6">
        <h1 className="text-2xl font-bold text-gray-800 text-center mb-6">Welcome Back!</h1>

        {successMessage && <p className="text-green-600 text-center mb-4 font-medium">{successMessage}</p>}
        {(authError || localError) && <p className="text-red-500 text-center mb-4 font-medium">{authError || localError}</p>}

        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label htmlFor="email" className="block text-sm font-medium text-gray-700">
              Email Address
            </label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="you@example.com"
              className="w-full mt-1 px-4 py-2 border rounded-lg shadow-sm focus:ring-2 focus:ring-blue-400 focus:outline-none"
            />
          </div>

          <div className="mb-6">
            <label htmlFor="password" className="block text-sm font-medium text-gray-700">
              Password
            </label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="********"
              className="w-full mt-1 px-4 py-2 border rounded-lg shadow-sm focus:ring-2 focus:ring-blue-400 focus:outline-none"
            />
          </div>

          <button
            type="submit"
            className="w-full bg-blue-500 text-white py-2 rounded-lg shadow-md hover:bg-blue-600 transition"
          >
            Login
          </button>
        </form>

        <div className="mt-4 text-center">
          <p className="text-gray-600">Don't have an account?</p>
          <button
            onClick={() => navigate("/register")}
            className="text-blue-500 hover:underline"
          >
            Register Here
          </button>
        </div>
      </div>
    </div>
  );
}

export default Login;
