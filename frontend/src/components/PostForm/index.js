import React, { useState } from "react";

import "./styles.css";

export default function DevForm({ onSubmit }) {
  const [search, setSearch] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();

    await onSubmit({
      search
    });
  }

  return (
    <form onSubmit={handleSubmit}>
      <div className="input-block">
        <label htmlFor="github_username">Título</label>
        <input
          name="title"
          id="title"
          value={search}
          onChange={e => setSearch(e.target.value)}
        />
      </div>
      <button type="submit"> Pesquisar </button>
    </form>
  );
}
