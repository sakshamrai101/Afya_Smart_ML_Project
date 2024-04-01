import React, { useState } from 'react'
import { Form, Button, Spinner, Card, ProgressBar } from 'react-bootstrap'
import { useNavigate } from 'react-router-dom'
import CustomNavbar from './components/Navbar'
import './ImportFile.css'

const ImportFile = () => {
  const [selectedFile, setSelectedFile] = useState(null)
  const [loading, setLoading] = useState(false)
  const [progress, setProgress] = useState(0) // State for progress
  const navigate = useNavigate()

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0])
  }

  const handleFileImport = async () => {
    if (selectedFile) {
      setLoading(true)
      // Simulate importing the PDF file
      let progressInterval = setInterval(() => {
        setProgress((prevProgress) => {
          if (prevProgress < 100) {
            return prevProgress + 10
          } else {
            clearInterval(progressInterval)
            setLoading(false)
            navigate('/service-types')
            return 100
          }
        })
      }, 150) // Simulating progress update every 500ms
    }
  }

  return (
    <>
      <CustomNavbar />
      <div className='d-flex justify-content-center align-items-center vh-100'>
        <Card className='import-container'>
          <Card.Body>
            <Card.Title>Reference E-consult Data</Card.Title>
            <div className='d-grid gap-2 d-md-block'>
              <Button className='bone-fracture' variant='primary' size='lg'>
                Bone Fracture
              </Button>
            </div>
            <div className='d-grid gap-2 d-md-block mt-2'>
              <Button className='oral-surgery' variant='secondary' size='lg'>
                Oral Surgery
              </Button>
            </div>
          </Card.Body>
          <Card.Body>
            <Card.Title>Import E-consult Data</Card.Title>
            {loading ? (
              <div className='text-center'>
                <Spinner animation='border' role='status'>
                  <span className='visually-hidden'>Loading...</span>
                </Spinner>
                Loading...
                <ProgressBar
                  now={progress}
                  label={`${progress}%`}
                  style={{
                    height: '30px',
                    fontSize: '16px',
                  }}
                  variant='warning'
                />
              </div>
            ) : (
              <>
                <div class='container mt-5'>
                  <div class='row'>
                    <div class='col-12 col-md-6 mb-2 mb-md-0'>
                      <Form.Group controlId='formFileLg'>
                        <Form.Control
                          type='file'
                          size='lg'
                          onChange={handleFileChange}
                          accept='.pdf,.docx,.txt'
                        />
                      </Form.Group>
                    </div>
                    <div class='col-12 col-md-6'>
                      <Button
                        className='import-button'
                        variant='primary'
                        type='submit'
                        onClick={handleFileImport}
                        disabled={!selectedFile || loading}
                      >
                        Upload
                      </Button>
                    </div>
                  </div>
                </div>
              </>
            )}
          </Card.Body>
        </Card>
      </div>
    </>
  )
}

export default ImportFile
