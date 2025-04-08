// src/pages/Chat.jsx
import React, { useState } from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const handleSend = () => {
    if (!input.trim()) return;

    setMessages([...messages, { role: "user", content: input }]);
    setInput("");
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-50 p-4">
      <div className="bg-white shadow-lg rounded-xl p-4 w-full max-w-md">
        <div className="space-y-4 max-h-[400px] overflow-y-auto">
          {messages.map((msg, idx) => (
            <div
              key={idx}
              className={`text-sm px-3 py-2 rounded-xl max-w-[80%] ${
                msg.role === "user" ? "bg-blue-100 self-end ml-auto text-right" : "bg-gray-200 self-start"
              }`}
            >
              {msg.content}
            </div>
          ))}
        </div>

        <div className="flex mt-4 gap-2">
          <Input
            placeholder="Введите ваше сообщение..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
            className="flex-grow"
          />
          <Button onClick={handleSend} disabled={!input.trim()}>
            Отправить
          </Button>
        </div>
      </div>
    </div>
  );
};

export default Chat;
