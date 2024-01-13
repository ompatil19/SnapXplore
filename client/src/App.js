import logo from './logo.svg';
// import './App.css';
import { ChakraProvider } from '@chakra-ui/react'
import Home from './components/home/Home';
import Recommendation from './components/reccomendation/Reccomendation'
import Uploader from './components/uploader/Uploader';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // Change 'Switch' to 'Routes'
function App() {
  return (
    <>
    <Router>
            <Routes>
                <Route path="/" element={<Home/>} />
                <Route path="/recommendations" element={<Recommendation/>} />
            </Routes>
    </Router>
    </>

  );
}

export default App;
