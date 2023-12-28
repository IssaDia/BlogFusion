import { createContext, useState, useContext, useEffect } from "react";

export const ArticleContext = createContext();
export const ArticleProvider = ({ children }) => {
  const [articles, setArticles] = useState([]);
  const [visitedArticles, setVisitedArticles] = useState(
    JSON.parse(localStorage.getItem("visitedArticles")) || {}
  );

  useEffect(() => {
    const fetchArticles = async () => {
      try {
        const response = await fetch("http://127.0.0.1:5000/api/articles");
        const data = await response.json();
        setArticles(data);
      } catch (error) {
        console.error("Error fetching articles:", error);
      }
      localStorage.setItem("visitedArticles", JSON.stringify(visitedArticles));
    };

    fetchArticles();
  }, [visitedArticles]);

  const markArticleAsVisited = (articleId) => {
    setVisitedArticles((prevVisited) => ({
      ...prevVisited,
      [articleId]: true,
    }));
    localStorage.setItem("visitedArticles", JSON.stringify(visitedArticles));
  };

  return (
    <ArticleContext.Provider
      value={{ articles, setArticles, visitedArticles, markArticleAsVisited }}
    >
      {children}
    </ArticleContext.Provider>
  );
};

export const useArticleContext = () => {
  return useContext(ArticleContext);
};
