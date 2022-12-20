import { useState, useEffect } from "react";
import reactLogo from "./assets/wik.png";
import "./css/App.css";
// i wanna use axios to make a request to the backend
import api from "./services/api";

interface WordProps {
  word: string;
  points: string;
  title: string;
  text: string;
}

function App() {
  const [word, setWord] = useState("");
  const [responseSearch, setResponseSearch] = useState([]);
  // const [searchFiltered, setSearchFiltered] = useState([]);

  const handleSubmit = (e: any) => {
    e.preventDefault();
    // searchWord(word);
    const size = word.split(" ").length;
    const words = word.split(" ");
    console.log("size", size);
    if (size === 1) {
      //se só houver uma palavra.
      api
        .get("/search", { headers: { word: word } })
        .then((res: any) => {
          console.log(res);
          if (res.data.data) {
            setResponseSearch(res.data.data);
            console.log("Response 1 palavra", res.data.data);
          }
        })
        .catch((err: ErrorCallback) => {
          console.log(err);
        });
    } else if (size === 2) {
      api
        .get("/findTwoWords", { headers: { word1: words[0], word2: words[1] } })
        .then((res: any) => {
          if (res.data.data) {
            setResponseSearch(res.data.data);
            console.log("Response 2 palavras", res.data.data);
          }
        })
        .catch((err: ErrorCallback) => {
          console.log(err);
        });
    }
  };

  useEffect(() => {
    const sorted = responseSearch.sort((a: any, b: any) => {
      return b.points - a.points;
    });

    const filtered = sorted.filter((item: any, index: number) => {
      return (
        sorted.findIndex((item2: any) => item2.title === item.title) === index
      );
    });

    setResponseSearch(filtered);
    console.log(responseSearch, "responseSearch");
  }, [responseSearch]);

  useEffect(() => {}, [responseSearch]);

  // useEffect(() => {
  //   api
  //     .get("/search", { headers: { word: word } })
  //     .then((res: any) => {
  //       if (res.data.data.length > 0 && responseSearch.length < 1) {
  //         setResponseSearch(res.data.data);
  //         console.log(res.data.data, "res.data.data");
  //       }
  //     })
  //     .catch((err: ErrorCallback) => {
  //       console.log(err);
  //     });

  //   const titles: string[] = [];
  //   if (responseSearch.length > 0) {
  //     responseSearch.forEach((item: WordProps) => {
  //       if (!titles.includes(item.title.toLowerCase()))
  //         titles.push(item.title.toLowerCase());
  //     });
  //     const filtered = responseSearch.filter((item: WordProps) => {
  //       return !(item.title.toLowerCase() in titles);
  //     });
  //     setSearchFiltered(filtered);
  //   }
  // }, [responseSearch]);

  // useEffect(() => {
  //   // setSearchFiltered(searchFiltered);
  // }, [searchFiltered, word]);

  // const searchWord = (wordParam: string) => {
  //   const size = wordParam.split(" ").length;
  //   let result = "";
  //   if (size === 1) {
  //     const filtered = responseSearch.filter((item: WordProps) => {
  //       return item.word.toLowerCase() === word.toLowerCase();
  //     });
  //     setSearchFiltered(filtered);
  //     // return filtered;
  //   } else {
  //     const words = word.split(" ");
  //     const filtered = responseSearch.filter((item: WordProps) => {
  //       return words.includes(item.word.toLowerCase());
  //     });

  //     setSearchFiltered(filtered);

  //     if (filtered.length < 1) {
  //       const filtered2 = responseSearch.filter((item: WordProps) => {
  //         return item.text.toLowerCase() === word.toLowerCase();
  //       });

  //       return filtered2;
  //     }
  //     return filtered;
  //   }
  // };

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
        <button type="submit" onClick={(e) => handleSubmit(e)}>
          Buscar
        </button>
      </div>
      <table>
        <thead>
          <tr>
            <th>Resultado</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            {responseSearch.length > 0 ? (
              <>
                {responseSearch.map((item: WordProps, index: number) => {
                  return (
                    <tr>
                      <td>ID: {index + 1}</td>
                      <td>{item.title}</td>
                      {/* <td>{item.word}</td>
                      <td>{item.points}</td> */}
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
