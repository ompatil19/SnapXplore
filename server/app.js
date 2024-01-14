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

const data = [{"imageurl": "https://source.unsplash.com/random", "category": "server did not repond", "location": "Server Error"},];

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
