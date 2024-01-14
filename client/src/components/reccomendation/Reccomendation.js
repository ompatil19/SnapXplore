import React from 'react'
import Card from '../utilities/card/Card'
import { useLocation } from 'react-router-dom';
import './reccom.css'
import seasons from '../../data/seasons.json'
import datas from '../../data/steams.json'
function Reccomendation() {
    const location = useLocation();
    let data = location.state?.data || datas
    const rand = Math.floor(Math.random() * 8);
    data=datas;
    return (
        <>
            <div className="recom-container">
               <a href="/"><h2 className="white">Snap<span className="orange">Xplore</span></h2></a> 
                <div className="row row-cols-auto justify-content-center">
                    {data.map((item, index) => (
                        <Card imageurl={item.imageurl} location={item.location} peak={seasons[rand].peak} moderate={seasons[rand].moderate} off={seasons[rand].off_season} />
                        )
                    )}
                </div>
            </div>
        </>
    );
}

export default Reccomendation