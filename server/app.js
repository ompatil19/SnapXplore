import express from 'express';
const app = express();
import {
    listOfFiles,
    UploadcareSimpleAuthSchema,
  } from '@uploadcare/rest-client';
  
const uploadcareSimpleAuthSchema = new UploadcareSimpleAuthSchema({
    publicKey: 'a389d59cb4735c200ff8',
    secretKey: '62a92102e9eb493b7921',
  });
  
app.get('/', (req, res) => {
    res.send('Hello, world!');
});


app.get('/snapimage', async (req, res) => {
    try {
      const result = await listOfFiles(
        {limit: 1,            
        ordering: '-datetime_uploaded'},
        { authSchema: uploadcareSimpleAuthSchema}
      );
      console.log(result.results[0].originalFileUrl);
      res.json(result);
    } catch (error) {
      console.error('Error:', error);
      res.status(500).send('Internal Server Error');
    }
  });


const port = 1900;
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
