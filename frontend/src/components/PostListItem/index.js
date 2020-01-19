import React from "react";
import { formatter } from "../../utils/date";
import "./styles.css";

const PostListItem = ({ post }) => {
  return (
    <li className="post-item">
      <div>
        <img src={post.img_url} alt={post.title} />
      </div>
      <p> {post.title}</p>
      <p className="date">
        Data de publicação: {formatter(post.published_date)}
      </p>
      <a href={`${post.post_url}`}>Acessar site</a>
    </li>
  );
};

export default PostListItem;
