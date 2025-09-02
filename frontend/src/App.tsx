import { ChakraProvider, Container, Heading, VStack } from '@chakra-ui/react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import PlanForm from './components/PlanForm';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <ChakraProvider>
        <Container maxW="container.lg" py={10}>
          <VStack spacing={8}>
            <Heading as="h1" size="2xl" textAlign="center">
              AI 驱动的自行车训练计划器
            </Heading>
            <PlanForm />
          </VStack>
        </Container>
      </ChakraProvider>
    </QueryClientProvider>
  );
}

export default App;