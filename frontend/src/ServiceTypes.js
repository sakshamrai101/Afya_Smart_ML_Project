import React, { useState } from 'react'
import { Button, Container, Card, Row, Col } from 'react-bootstrap'
import './ServiceTypes.css'
import CustomNavbar from './components/Navbar'

const ServiceTypes = () => {
  const [disabledButtons, setDisabledButtons] = useState({
    'show-missing-information': false,
    'generate-targeted-questions': false,
    'display-recommendations': false,
  })

  const handleClick = (buttonName) => {
    setDisabledButtons((prevDisabledButtons) => ({
      ...prevDisabledButtons,
      [buttonName]: true,
    }))
  }

  return (
    <>
      <CustomNavbar />
      <div className='d-flex justify-content-center align-items-center vh-100'>
        <Card className='service-container'>
          <Card.Body>
            <h1 className='title'>Service Types</h1>
            <Container className='center'>
              <Row className='justify-content-center'>
                <Col xs='auto' className='mb-2'>
                  <Button
                    variant='primary'
                    size='lg'
                    className='mb-2'
                    style={{ marginRight: '10px' }}
                    disabled={disabledButtons['show-missing-information']}
                    onClick={() => handleClick('show-missing-information')}
                  >
                    Show Missing Information
                  </Button>
                </Col>
              </Row>
              <Row className='justify-content-center'>
                <Col xs='auto' className='mb-2'>
                  <Button
                    variant='primary'
                    size='lg'
                    className='mb-2'
                    style={{ marginRight: '10px' }}
                    disabled={disabledButtons['generate-targeted-questions']}
                    onClick={() => handleClick('generate-targeted-questions')}
                  >
                    Generate Targeted Questions
                  </Button>
                </Col>
              </Row>
              <Row className='justify-content-center'>
                <Col xs='auto' className='mb-2'>
                  <Button
                    variant='primary'
                    size='lg'
                    className='mb-2'
                    disabled={disabledButtons['display-recommendations']}
                    onClick={() => handleClick('display-recommendations')}
                  >
                    Display Recommendations
                  </Button>
                </Col>
              </Row>
            </Container>
          </Card.Body>
        </Card>
      </div>
    </>
  )
}

export default ServiceTypes
