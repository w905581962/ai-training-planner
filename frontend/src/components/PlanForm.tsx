import { useState } from 'react';
import {
  Box, Button, FormControl, FormLabel, Input, Select, VStack, useToast, Spinner, Text,
  NumberInput, NumberInputField, NumberInputStepper, NumberIncrementStepper, NumberDecrementStepper,
  SimpleGrid, Card, CardHeader, Heading, CardBody, Stack, StackDivider,
} from '@chakra-ui/react';
import { useMutation } from '@tanstack/react-query';
import axios from 'axios';
import CalendarView from './CalendarView';

// 为响应数据定义类型
interface WorkoutBlock {
  type: string;
  duration_seconds: number;
  power_start_percent_ftp: number;
}

interface DailyWorkout {
  day: string;
  title: string;
  coach_notes: string;
  blocks: WorkoutBlock;
}

interface TrainingPlan {
  plan_name: string;
  workouts: DailyWorkout[];
}

const PlanForm = () => {
  const [athleteId, setAthleteId] = useState('');
  const [apiKey, setApiKey] = useState('');
  const [goal, setGoal] = useState('提升FTP');
  const [weeks, setWeeks] = useState(4);
  const [daysPerWeek, setDaysPerWeek] = useState(3);
  const [hoursPerWeek, setHoursPerWeek] = useState(5);
  const [generatedPlan, setGeneratedPlan] = useState<TrainingPlan | null>(null);

  const toast = useToast();

  const mutation = useMutation({
    mutationFn: (newPlanRequest: any) => {
      // 在生产环境中，这应该是相对路径或通过环境变量配置
      return axios.post('/api/v1/generate-and-upload', newPlanRequest);
    },
    onSuccess: (data) => {
      setGeneratedPlan(data.data.plan_details);
      toast({
        title: '计划已生成并上传！',
        description: "您的新训练计划已发送到您的 intervals.icu 日历。",
        status: 'success',
        duration: 9000,
        isClosable: true,
      });
    },
    onError: (error: any) => {
      toast({
        title: '发生错误。',
        description: error.response?.data?.detail || error.message,
        status: 'error',
        duration: 9000,
        isClosable: true,
      });
    },
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setGeneratedPlan(null);
    mutation.mutate({ athlete_id: athleteId, api_key: apiKey, goal, weeks, days_per_week: daysPerWeek, hours_per_week: hoursPerWeek });
  };

  return (
    <Box w="100%">
      <form onSubmit={handleSubmit}>
        <VStack spacing={4} align="stretch" p={8} borderWidth={1} borderRadius="lg" boxShadow="lg">
          <Heading size="md" mb={4}>1. 输入您的信息</Heading>
          <FormControl isRequired>
            <FormLabel>Intervals.icu 运动员 ID</FormLabel>
            <Input value={athleteId} onChange={(e) => setAthleteId(e.target.value)} placeholder="例如, i12345" />
          </FormControl>
          <FormControl isRequired>
            <FormLabel>Intervals.icu API 密钥</FormLabel>
            <Input type="password" value={apiKey} onChange={(e) => setApiKey(e.target.value)} placeholder="您的 API 密钥" />
          </FormControl>

          <Heading size="md" mt={6} mb={4}>2. 定义您的训练</Heading>
          <FormControl isRequired>
            <FormLabel>主要目标</FormLabel>
            <Select value={goal} onChange={(e) => setGoal(e.target.value)}>
              <option value="提升FTP">提升FTP</option>
              <option value="备战山区长距离挑战赛">山区长距离挑战赛</option>
              <option value="备战绕圈赛">绕圈赛</option>
              <option value="建立有氧基础">建立有氧基础</option>
            </Select>
          </FormControl>
          <SimpleGrid columns={3} spacing={4}>
            <FormControl>
              <FormLabel>周数</FormLabel>
              <NumberInput value={weeks} onChange={(_, val) => setWeeks(val)} min={1} max={24}>
                <NumberInputField />
                <NumberInputStepper><NumberIncrementStepper /><NumberDecrementStepper /></NumberInputStepper>
              </NumberInput>
            </FormControl>
            <FormControl>
              <FormLabel>天/周</FormLabel>
              <NumberInput value={daysPerWeek} onChange={(_, val) => setDaysPerWeek(val)} min={1} max={7}>
                <NumberInputField />
                <NumberInputStepper><NumberIncrementStepper /><NumberDecrementStepper /></NumberInputStepper>
              </NumberInput>
            </FormControl>
            <FormControl>
              <FormLabel>小时/周</FormLabel>
              <NumberInput value={hoursPerWeek} onChange={(_, val) => setHoursPerWeek(val)} min={1} max={30}>
                <NumberInputField />
                <NumberInputStepper><NumberIncrementStepper /><NumberDecrementStepper /></NumberInputStepper>
              </NumberInput>
            </FormControl>
          </SimpleGrid>

          <Button type="submit" colorScheme="blue" isLoading={mutation.isPending} mt={6}>
            生成并上传计划
          </Button>
        </VStack>
      </form>

      {mutation.isPending && (
        <VStack mt={8}>
          <Spinner size="xl" />
          <Text>AI 正在为您精心打造计划... 这可能需要一点时间。</Text>
        </VStack>
      )}

      {generatedPlan && (
        <Box mt={10}>
          <Heading size="lg" mb={4}>{generatedPlan.plan_name}</Heading>
          <CalendarView workouts={generatedPlan.workouts} />
          
          <Heading size="lg" mt={10} mb={4}>训练详情</Heading>
          {generatedPlan.workouts.map(workout => (
            <Card key={workout.day} mb={4}>
              <CardHeader>
                <Heading size='md'>{workout.day}: {workout.title}</Heading>
              </CardHeader>
              <CardBody>
                <Stack divider={<StackDivider />} spacing='4'>
                  <Box>
                    <Heading size='xs' textTransform='uppercase'>教练笔记</Heading>
                    <Text pt='2' fontSize='sm'>{workout.coach_notes}</Text>
                  </Box>
                </Stack>
              </CardBody>
            </Card>
          ))}
        </Box>
      )}
    </Box>
  );
};

export default PlanForm;