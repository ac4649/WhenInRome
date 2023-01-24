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
            <Box align="center">
                <Text weight="bold"> 
                    { props.formTitle }
                </Text>
            </Box>
            <Form
                onSubmit={onSubmit}
                onChange={value => setValue(value)}
                value={value}
            >
                <Box gap="small">
                    <Box direction="row-responsive" gap="small">
                        <Box gap="small">
                            <FormField name="numeral1" label="Roman Numeral 1 (Viniculum Notation)" help="Add _ before a letter I or X to multiply it by 1,000" required>
                                <TextInput 
                                    name="numeral1"
                                />
                            </FormField>
                            <ShowUpperBars value={value.numeral1} />
                        </Box>
                        <Box gap="small">
                            <FormField name="numeral2" label="Roman Numeral 2 (Viniculum Notation)" help="Add _ before a letter I or X to multiply it by 1,000" required>
                                <TextInput 
                                    name="numeral2"
                                />
                            </FormField>
                            <ShowUpperBars value={value.numeral2} />
                        </Box>
                    </Box>
                    <Button primary type="submit" label="Add!"/>
                </Box>
            </Form>

            {
                value.sum && (
                    <Box>
                        <ShowUpperBars title="Result:" value={value.sum} />
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