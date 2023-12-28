import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useArticleContext } from "./context/ArticleContext";

const ArticleDetail = () => {
  const { slug } = useParams();
  const { articles } = useArticleContext();

  const filteredArticle = articles.find((article) => article.slug === slug);

  return (
    <div className="container mx-auto p-8">
      {filteredArticle && (
        <div className="max-w-6xl mx-auto bg-white p-8 rounded-md shadow-md">
          <h2 className="text-3xl font-bold mb-4">{filteredArticle.title}</h2>
          <div
            className="content"
            dangerouslySetInnerHTML={{ __html: filteredArticle.content }}
          />
        </div>
      )}
      {!filteredArticle && <p>Article not found</p>}
    </div>
  );
};

export default ArticleDetail;
