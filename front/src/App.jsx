import React, { useState, useEffect, useContext } from "react";
import { useParams, Routes, Route, Link } from "react-router-dom";
import { useArticleContext } from "./components/context/ArticleContext";
import "./App.css";
function App() {
  const { articles, visitedArticles, markArticleAsVisited } =
    useArticleContext();

  return (
    <div className="container mx-auto p-8">
      <div className="mt-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {articles.map((article) => (
          <div
            key={article.id}
            className="border border-gray-300 p-4 rounded-md mb-4"
          >
            <h2 className="text-xl font-bold mb-2">{article.title}</h2>
            <Link
              to={`/article/${article.slug}`}
              className="text-blue-500 hover:underline block mt-2"
              onClick={() => markArticleAsVisited(article.id)}
            >
              Lire l'article
            </Link>
            {visitedArticles[article.id] && (
              <span className="text-green-500 block mt-2">
                {" "}
                ✓ Article visité
              </span>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
