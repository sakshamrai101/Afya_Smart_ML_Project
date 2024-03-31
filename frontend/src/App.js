import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './App.css'
import ImportFile from './ImportFile'
import ServiceTypes from './ServiceTypes'
import ShowMissingInfo from './ShowMissingInfo'
import 'bootstrap/dist/css/bootstrap.min.css'

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<ImportFile />} />
        <Route path='/service-types' element={<ServiceTypes />} />
        <Route path='/show-missing-information' element={<ShowMissingInfo />} />
      </Routes>
    </Router>
  )
}

export default App
