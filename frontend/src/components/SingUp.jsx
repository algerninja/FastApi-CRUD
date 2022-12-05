import { useNavigate } from "react-router";
import { fetchToken, setToken } from "../utils/Auth";
import { useState } from "react";
import axios from "axios";

export default function Login() {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [password, setPassword] = useState("");

  //check to see if the fields are not empty
  const singup = () => {
    if (
      (email == "") &
      (firstName == "") &
      (lastName == "") &
      (password == "")
    ) {
      return;
    } else {
      // make api call to our backend. we'll leave thisfor later
      axios
        .post("http://localhost:8000/singup", {
          email: email,
          firstname: firstName,
          lastname: lastName,
          password: password,
        })
        .then(function (response) {
          console.log(response);
          if (response) {
            navigate("/");
          }
        })
        .catch(function (error) {
          console.log(error, "error");
        });
    }
  };

  return (
    <div style={{ minHeight: 800, marginTop: 30 }}>
      <h1>Sing Up Page</h1>
      <div style={{ marginTop: 30 }}>
        {fetchToken() ? (
          <p>you are logged in</p>
        ) : (
          <div>
            <form>
              <label style={{ marginRight: 10 }}>Input Email</label>
              <input type="text" onChange={(e) => setEmail(e.target.value)} />
              <label style={{ marginRight: 10 }}>Input First Name</label>
              <input
                type="text"
                onChange={(e) => setFirstName(e.target.value)}
              />
              <label style={{ marginRight: 10 }}>Input Last Name</label>
              <input
                type="text"
                onChange={(e) => setLastName(e.target.value)}
              />

              <label style={{ marginRight: 10 }}>Input Password</label>
              <input
                type="text"
                onChange={(e) => setPassword(e.target.value)}
              />

              <button type="button" onClick={singup}>
                Sing Up
              </button>
            </form>
          </div>
        )}
      </div>
    </div>
  );
}
