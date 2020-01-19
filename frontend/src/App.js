import React, { useState, useEffect } from "react";
import api from "./services/api";

import "./global.css";
import "./App.css";
import "./Sidebar.css";
import "./Main.css";

import PostListItem from "./components/PostListItem";
import PostForm from "./components/PostForm";

function App() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    async function loadPosts() {
      const response = await api.get("posts");
      setPosts(response.data);
    }

    loadPosts();
  }, []);

  async function handleSubmit(dados) {
    const response = await api.get("posts", { params: dados });

    setPosts(response.data);
  }
  return (
    <div id="app">
      <aside>
        <strong>Notícias de Tecnologia</strong>
        <PostForm onSubmit={handleSubmit} />
      </aside>
      <main>
        {posts.length !== 0 ? (
          <ul>
            {posts.map(post => (
              <PostListItem key={post.id} post={post} />
            ))}
          </ul>
        ) : (
          <div className="no-data">Notícia não encontrada</div>
        )}
      </main>
    </div>
  );
}

export default App;
