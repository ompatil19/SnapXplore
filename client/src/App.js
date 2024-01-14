import './App.css';
import Home from './components/home/Home';
import Recommendation from './components/reccomendation/Reccomendation'
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
