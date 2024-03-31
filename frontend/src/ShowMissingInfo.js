import React from 'react'
import { Card, Button, Form } from 'react-bootstrap'

const ShowMissingInfo = () => {
  const handleSubmit = (e) => {
    e.preventDefault()
    // Submit the information back to the database
    console.log('Submitting information...')
  }

  return (
    <div>
      <h1>Missing Information</h1>
      <Card style={{ width: '30rem', margin: '0 auto' }}>
        <Card.Body>
          <Card.Title>Missing Information</Card.Title>
          <Form>
            <Form.Check type='checkbox' label='Name' />
            <Form.Check type='checkbox' label='Age' />
            <Form.Check type='checkbox' label='Gender' />
            {/* Add more Form.Check elements for other missing information */}
          </Form>
          <Button variant='primary' style={{ marginRight: '10px' }}>
            Edit
          </Button>
          <Button variant='success' onClick={handleSubmit}>
            Done
          </Button>
        </Card.Body>
      </Card>
    </div>
  )
}

export default ShowMissingInfo
