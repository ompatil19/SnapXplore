import React from 'react'
import './card.css'
function Card(props) {
  const imageurl = props.imageurl;
  return (
    <div class="card">
  <div class="card-image-container">
    {/* <svg
      xmlns="http://www.w3.org/2000/svg"
      width="1em"
      height="1em"
      viewBox="0 0 1024 1024"
      stroke-width="0"
      fill="currentColor"
      stroke="currentColor"
      class="image-icon"
    >
      <path
        d="M928 160H96c-17.7 0-32 14.3-32 32v640c0 17.7 14.3 32 32 32h832c17.7 0 32-14.3 32-32V192c0-17.7-14.3-32-32-32zM338 304c35.3 0 64 28.7 64 64s-28.7 64-64 64-64-28.7-64-64 28.7-64 64-64zm513.9 437.1a8.11 8.11 0 0 1-5.2 1.9H177.2c-4.4 0-8-3.6-8-8 0-1.9.7-3.7 1.9-5.2l170.3-202c2.8-3.4 7.9-3.8 11.3-1 .3.3.7.6 1 1l99.4 118 158.1-187.5c2.8-3.4 7.9-3.8 11.3-1 .3.3.7.6 1 1l229.6 271.6c2.6 3.3 2.2 8.4-1.2 11.2z"
      ></path>
    </svg> */}
    <img src={imageurl} alt="" />
  </div>
  <p class="card-title">{props.location}</p>
  <p class="card-des">
    <div className="location">{}</div>
    <div className="distance">{props.category}</div>
    <div className="season-box d-flex flex-row justify-content-around align-items-center py-3 text-center">
        <div className="season green"><p>Peak</p><p>{props.peak}</p></div>
        <div className="season yellow"><p>Moderate</p><p>{props.moderate}</p></div>
        <div className="season red"><p>Off</p><p>{props.off}</p></div>    
    </div>
  </p>
</div>

  )
}

export default Card