import { AxiosResponse } from "axios";
import { Box, BoxProps, Button, Form, FormExtendedEvent, FormField, Text, TextInput } from "grommet"
import React from "react"
import ShowUpperBars from "./ShowUpperBars";
const axios = require('axios');

interface IRomanAdditionForm {
    formTitle: string
    formBoxProps : BoxProps
}

interface IFormValue {
    numeral1: string
    numeral2: string
    sum ? : string
    error ? : string
}

const RomanAdditionForm = ( props : IRomanAdditionForm ) => {

    const [value, setValue] = React.useState<IFormValue>({numeral1: "", numeral2: ""})

    const onSubmit = ( event: FormExtendedEvent<IFormValue, Element> ) => {
        let newValue : IFormValue = {
            numeral1 : event.value.numeral1,
            numeral2 : event.value.numeral2
        }
        axios.get("/api/romanAddition?numeral1=" + event.value.numeral1 + "&numeral2=" + event.value.numeral2).then(
            (response : AxiosResponse) => {

                if (response.data.sum) {
                    newValue.sum = response.data.sum
                } else {
                    if (response.data.error) {
                        newValue.error = response.data.error
                    }
                }

                setValue(newValue)
            }
        )
    }

    return (
        <Box {...props.formBoxProps} >
            <Text> 
                { props.formTitle }
            </Text>
            <Form
                onSubmit={onSubmit}
                onChange={value => setValue(value)}
                value={value}
            >
                <Box gap="small">
                    <Box direction="row-responsive">
                        <Box gap="small">
                            <FormField name="numeral1" label="Roman Numeral (Viniculum Notation)" help="Add _ before a letter I or X to multiply it by 1,000" required>
                                <TextInput 
                                    name="numeral1"
                                />
                            </FormField>
                            <Box border="all" pad="small">
                                Preview of the text with bars on top
                                &nbsp;
                                <ShowUpperBars value={value.numeral1} />
                            </Box>
                        </Box>
                        <Box gap="small">
                            <FormField name="numeral2" label="Roman Numeral (Viniculum Notation)" help="Add _ before a letter I or X to multiply it by 1,000" required>
                                <TextInput 
                                    name="numeral2"
                                />
                            </FormField>
                            <Box border="all" pad="small">
                                Preview of the text with bars on top
                                &nbsp;
                                <ShowUpperBars value={value.numeral2} />
                            </Box>
                        </Box>
                    </Box>
                    <Button primary type="submit" label="Convert!"/>
                </Box>
            </Form>

            {
                value.sum && (
                    <Box>
                        <ShowUpperBars value={value.sum} />
                    </Box>
                )
            }
            {
                value.error && (
                    <Box>
                        <Text color="red">{value.error}</Text>
                    </Box>
                )
            }
        </Box>
    )
}

export default RomanAdditionForm
export { RomanAdditionForm as RomanAdditionForm }