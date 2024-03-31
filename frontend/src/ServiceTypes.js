import React from 'react'
import { Link } from 'react-router-dom'
import { Button, Container } from 'react-bootstrap'
import './ServiceTypes.css'

const ServiceTypes = () => {
  return (
    <>
      <h1 className='title'>Service Types</h1>
      <Container className='center'>
        <Button as={Link} to='/show-missing-information' variant='primary'>
          Show Missing Information
        </Button>{' '}
        <Button as={Link} to='/generate-targeted-questions' variant='primary'>
          Generate Targeted Questions
        </Button>{' '}
        <Button as={Link} to='/display-recommendations' variant='primary'>
          Display Recommendations
        </Button>{' '}
      </Container>
    </>
  )
}

export default ServiceTypes
