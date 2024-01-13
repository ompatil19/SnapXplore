import React from 'react'
import {useNavigate } from 'react-router-dom';
import Uploader from '../uploader/Uploader'
import bgimage from '../../images/background.jpg'
import axios from 'axios'
import './home.css'
function Home() {   
    const navigate = useNavigate();

    const recommendPlaces = async () => {
        try {
            const response = await axios.get('http://localhost:1900/reccomimage');
            navigate('/recommendations', { state: { data: response.data } });
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };
    return (
        <>  
            <div className="d-flex flex-row main-box">
                <div className="d-flex flex-column left align-items-start justify-content-center px-5">
                    <h1 className="heading font-bold text-white">Snap<span className="orange">Xplore</span></h1>
                    <h2 className="slogan font-bold text-white">Capture Discover Explore</h2>
                </div>  
                <div className="d-flex flex-column right justify-content-center align-items-center ">
                    <Uploader />
                    <p className="text-2xl font-bold text-white fs-4 py-2 fst-italic">Upload all your <span className="orange"> travel pictures </span> here</p>
                    <button onClick={recommendPlaces} className='send-button'>
                        <div class="svg-wrapper-1">
                            <div class="svg-wrapper">
                                <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    viewBox="0 0 24 24"
                                    width="24"
                                    height="24"
                                >
                                    <path fill="none" d="M0 0h24v24H0z"></path>
                                    <path
                                        fill="currentColor"
                                        d="M1.946 9.315c-.522-.174-.527-.455.01-.634l19.087-6.362c.529-.176.832.12.684.638l-5.454 19.086c-.15.529-.455.547-.679.045L12 14l6-8-8 6-8.054-2.685z"
                                    ></path>
                                </svg>
                            </div>
                        </div>
                        <span>Send</span>
                    </button>

                </div>
            </div>
        </>
    )
}

export default Home