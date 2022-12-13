import { useState, useEffect } from "react";
import reactLogo from "./assets/wik.png";
import "./css/App.css";
// i wanna use axios to make a request to the backend
import api from "./services/api";

interface WordProps {
  word: string;
  points: string;
}

function App() {
  const [count, setCount] = useState(0);
  const [word, setWord] = useState("");
  const [responseSearch, setResponseSearch] = useState([]);

  const handleSubmit = (e: any) => {
    e.preventDefault();
    api
      .get("/search", { headers: { word: word } })
      .then((res: any) => {
        setResponseSearch(res.data.data);
        // console.log(res.data);
      })
      .catch((err: ErrorCallback) => {
        console.log(err);
      });
  };

  useEffect(() => {
    console.log(responseSearch);
  }, [responseSearch]);

  return (
    <div className="App">
      <div>
        <a href="https://vitejs.dev" target="_blank">
          {/* <img src={reactLogo} className="logo" alt="Vite logo" /> */}
        </a>
        <a>
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Buscador Hipermidiático</h1>
      <div className="card">
        <input
          placeholder="Palavra Desejada"
          onChange={(e) => setWord(e.target.value)}
        ></input>
        <button onClick={(e) => handleSubmit(e)}>Buscar</button>
      </div>
      {/* i wanna show the results of search request on a table */}
      <table>
        <thead>
          <tr>
            <th>Resultado</th>
            {/* <th>Arquivo</th> */}
            {/* <th>Posição</th> */}
          </tr>
        </thead>
        <tbody>
          <tr>
            {/* map the response */}
            {responseSearch.length > 0 ? (
              <>
                {responseSearch.map((item: WordProps) => {
                  return (
                    <tr>
                      <td>{item.word}</td>
                      <td>{item.points}</td>
                    </tr>
                  );
                })}
              </>
            ) : (
              <></>
            )}
          </tr>
        </tbody>
      </table>
      <p className="read-the-docs">github.com/pvborgesz</p>
    </div>
  );
}

export default App;
