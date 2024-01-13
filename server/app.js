import express from 'express';
import cors from 'cors';
const app = express();
app.use(cors());
import {
  listOfFiles,
  UploadcareSimpleAuthSchema,
} from '@uploadcare/rest-client';
import axios from 'axios';

const uploadcareSimpleAuthSchema = new UploadcareSimpleAuthSchema({
  publicKey: 'a389d59cb4735c200ff8',
  secretKey: '62a92102e9eb493b7921',
});

app.get('/', (req, res) => {
  res.send('Hello, world!');
});

const data = [
  { imageurl: "https://source.unsplash.com/random", name: "Om Beach", location: "Gokarna, Karnataka", distance: "200kms" },
  { imageurl: "https://source.unsplash.com/random", name: "JPG Beach", location: "JPG City", distance: "300kms" },
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

app.get('/reccomimage', async (req, res) => {
  try {
    const result = await listOfFiles(
      {
        limit: 1,
        ordering: '-datetime_uploaded'
      },
      { authSchema: uploadcareSimpleAuthSchema }
    );
    console.log(result.results[0].originalFileUrl);
    const finalurl = result.results[0].originalFileUrl;
    const apiUrl = 'https://example.com/your-endpoint'; 
    const response = await axios.get(apiUrl, {
      params: {
        finalurl: finalurl
      }
    });
    const responseData = response.data;
    res.json(responseData);
  } catch (error) {
    console.error('Error:', error);
    res.send(data);
  }
});


const port = 1900;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
