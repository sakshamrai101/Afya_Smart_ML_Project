import React, { useState } from 'react'
import { Form, Button, Spinner, Container, ProgressBar } from 'react-bootstrap'
import { useNavigate } from 'react-router-dom'
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
      }, 500) // Simulating progress update every 500ms
    }
  }

  return (
    <Container className='import-container'>
      <Form.Group controlId='formFileLg' className='mb-3'>
        <Form.Label>Import PDF File</Form.Label>
        <Form.Control
          type='file'
          size='lg'
          onChange={handleFileChange}
          accept='.pdf,.docx,.txt'
        />
      </Form.Group>
      <Button
        className='import-button'
        variant='primary'
        type='submit'
        onClick={handleFileImport}
        disabled={!selectedFile || loading}
      >
        {loading ? (
          <>
            <Spinner
              as='span'
              animation='border'
              size='sm'
              role='status'
              aria-hidden='true'
            />
            Loading...
            <ProgressBar now={progress} label={`${progress}%`} />
          </>
        ) : (
          'Upload'
        )}
      </Button>
    </Container>
  )
}

export default ImportFile
