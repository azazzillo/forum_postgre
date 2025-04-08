import React from "react";
import { useNavigate, useLocation, Link } from "react-router-dom";

function Navbar() {
  const navigate = useNavigate();
  const location = useLocation();

  // Скрываем Navbar на главной и странице регистрации
  if (location.pathname === '/' || location.pathname === '/register') {
    return null;
  }

  const handleLogout = () => {
    localStorage.removeItem('accessToken');
    navigate('/');
  };

  return (
    <header className="fixed top-0 left-0 right-0 z-50 bg-white shadow-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Лого или название сайта */}
          <Link to="/profile" className="text-xl font-bold text-blue-600 hover:text-blue-700 transition">
            MANDARIN
          </Link>

          {/* Навигационные ссылки */}
          <nav className="flex items-center space-x-6">
            <Link
              to="/profile"
              className="text-gray-700 hover:text-orange-600 transition font-medium"
            >
              Profile
            </Link>
            <Link
              to="/chat"
              className="text-gray-700 hover:text-orange-600 transition font-medium"
            >
              Chat
            </Link>
            <button
            onClick={handleLogout}
            className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-1.5 rounded-xl shadow transition cursor-pointer"
            >
            Logout
            </button>

          </nav>
        </div>
      </div>
    </header>
  );
}

export default Navbar;
