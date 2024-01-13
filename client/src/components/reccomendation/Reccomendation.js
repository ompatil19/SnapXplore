import React from 'react'
import Card from '../utilities/card/Card'
import { useLocation } from 'react-router-dom';
import './reccom.css'
function Reccomendation() {
    const location = useLocation();
    const data = location.state?.data || [
        { imageurl: "https://source.unsplash.com/random", name: "Omnom Beach", location: "Gokarna, Karnataka", distance: "200kms" },
        { imageurl: "https://source.unsplash.com/random", name: "JPGreccom Beach", location: "JPG City", distance: "300kms" },
        { imageurl: "https://source.unsplash.com/random", name: "Sunset Cove", location: "Island Paradise", distance: "150kms" },
        { imageurl: "https://source.unsplash.com/random", name: "Moonlight Bay", location: "Dreamland", distance: "400kms" },
        { imageurl: "https://source.unsplash.com/random", name: "Golden Shore", location: "Golden Coast", distance: "250kms" },
        { imageurl: "https://source.unsplash.com/random", name: "Silver Sands", location: "Silver City", distance: "180kms" },
        { imageurl: "https://source.unsplash.com/random", name: "Mystic Beach", location: "Enchanted Land", distance: "320kms" },
        { imageurl: "https://source.unsplash.com/random", name: "Emerald Cove", location: "Secret Retreat", distance: "280kms" },
        { imageurl: "https://source.unsplash.com/random", name: "Sapphire Shores", location: "Blue Haven", distance: "220kms" },
        { imageurl: "https://source.unsplash.com/random", name: "Diamond Dunes", location: "Luxury Oasis", distance: "350kms" },
        { imageurl: "https://source.unsplash.com/random", name: "Crimson Coast", location: "Red City", distance: "270kms" },
        { imageurl: "https://source.unsplash.com/random", name: "Azure Bay", location: "Azure Paradise", distance: "230kms" },
        { imageurl: "https://source.unsplash.com/random", name: "Velvet Beach", location: "Velvet Town", distance: "290kms" },
        { imageurl: "https://source.unsplash.com/random", name: "Platinum Sands", location: "Platinum Resort", distance: "180kms" },
        { imageurl: "https://source.unsplash.com/random", name: "Radiant Retreat", location: "Sunshine Haven", distance: "400kms" },
    ];
    return (
        <>
            <div className="recom-container">
                <h2 className="white">Snap<span className="orange">Xplore</span> Recommendations</h2>
                <div className="row row-cols-auto justify-content-center">
                    {data.map((item, index) => (
                        <Card imageurl={item.imageurl} name={item.name} location={item.location} distance={item.distance} />
                    ))}
                </div>
            </div>
        </>
    );
}

export default Reccomendation