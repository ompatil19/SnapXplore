import React from 'react'
import { Container } from '@chakra-ui/react'
import { Stack, HStack, VStack } from '@chakra-ui/react'
import { Heading } from '@chakra-ui/react'
import { Text } from '@chakra-ui/react'
import { Flex, Spacer } from '@chakra-ui/react'
import Uploader from '../uploader/Uploader'
import bgimage from '../../images/background.jpg'
import './home.css'
function Home() {      
    return (
        //     <Container
        //   maxW="100vw"
        //   h="100vh" bg="#1d1b1b">
        //     <Flex h="100vh" py={20}>
        //       <VStack w="full" h="full" p={10} spacing={10} alignItems="flex-start" justifyContent="center" >
        //         {/* <Text color="white">Hello</Text> */}
        //         <Heading size="4xl" color="white">Snap<span color='#e28238'>Explore</span> </Heading>
        //         <Text fontSize="4xl" color="#e28238">Capture Discover Explore</Text>
        //       </VStack>
        //       <VStack w="full" h="full" p={10} spacing={4} alignItems="center" justifyContent="center" >
        //         {/* <Text color="white">Hello</Text> */}
        //         <Uploader/>
        //         <Text color="#e28238" as="i">Upload all your travel pictures here</Text>
        //       </VStack>
        //     </Flex>
        //     </Container>
        <>  
            <div className="d-flex flex-row main-box">
                <div className="d-flex flex-column left align-items-start justify-content-center px-5">
                    <h1 className="heading font-bold text-white">Snap<span className="orange">Xplore</span></h1>
                    <h2 className="slogan font-bold text-white">Capture Discover Explore</h2>
                </div>  
                <div className="d-flex flex-column right justify-content-center align-items-center ">
                    <Uploader />
                    <p className="text-2xl font-bold text-white fs-4 py-2 fst-italic">Upload all your <span className="orange"> travel pictures </span> here</p>
                    <button className='send-button'>
                        <div class="svg-wrapper-1">
                            <div class="svg-wrapper">
                                <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    viewBox="0 0 24 24"
                                    width="24"
                                    height="24"
                                >
                                    <path fill="none" d="M0 0h24v24H0z"></path>
                                    <path
                                        fill="currentColor"
                                        d="M1.946 9.315c-.522-.174-.527-.455.01-.634l19.087-6.362c.529-.176.832.12.684.638l-5.454 19.086c-.15.529-.455.547-.679.045L12 14l6-8-8 6-8.054-2.685z"
                                    ></path>
                                </svg>
                            </div>
                        </div>
                        <span>Send</span>
                    </button>

                </div>
            </div>
        </>
    )
}

export default Home