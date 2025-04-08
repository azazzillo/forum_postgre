import React, { useEffect, useState } from "react";
import { motion } from "framer-motion";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Profile() {
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("accessToken");
    if (!token) {
      navigate("/"); // если не авторизован — на логин
      return;
    }

    axios.get("http://localhost:8080/me", {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    .then((res) => {
      setUser(res.data);
    })
    .catch((err) => {
      console.error("Ошибка при получении профиля:", err);
      navigate("/"); // токен невалиден или просрочен
    });
  }, []);

  if (!user) return <div className="text-center p-4">Загрузка...</div>;

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-100 to-white p-6">
      <motion.div
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.4 }}
        className="bg-white rounded-2xl shadow-2xl p-8 max-w-md w-full text-center"
      >
        <div className="w-24 h-24 mx-auto mb-4">
          <div className="w-full h-full rounded-full bg-blue-400 flex items-center justify-center text-white text-3xl font-semibold">
            {user.name ? user.name[0] : "?"}
          </div>
        </div>
        <h2 className="text-2xl font-bold text-gray-800 mb-1">{user.name}</h2>
        <p className="text-gray-600 text-sm mb-2">@{user.username}</p>
        <p className="text-gray-500">{user.email}</p>
      </motion.div>
    </div>
  );
}

export default Profile;
