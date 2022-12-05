import "./App.css";

import { Routes, Route } from "react-router-dom";
import Login from "./components/Login";
import Profile from "./components/Profile";
import SingUp from "./components/SingUp";
import { RequireToken } from "./utils/Auth";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Login />} />
        <Route
          path="/profile"
          element={
            <RequireToken>
              <Profile />
            </RequireToken>
          }
        />
        <Route path="/singup" element={<SingUp />} />
      </Routes>
    </div>
  );
}

export default App;
