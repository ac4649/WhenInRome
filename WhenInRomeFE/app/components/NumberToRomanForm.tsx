import { AxiosResponse } from "axios";
import { Box, BoxProps, Button, Form, FormExtendedEvent, FormField, Text, TextInput } from "grommet"
import React from "react"
const axios = require('axios');

interface IRomanToNumberForm {
    formTitle: string
    formBoxProps : BoxProps
}

interface IFormValue {
    number ? : number
    numeral ? : string
    error ? : string
}

const NumberToRomanForm = ( props : IRomanToNumberForm ) => {

    const [value, setValue] = React.useState<IFormValue>({})

    const onSubmit = ( event: FormExtendedEvent<IFormValue, Element> ) => {
        let newValue : IFormValue = {
            number : event.value.number
        }
        axios.get("/api/numberToNumeral?number=" + event.value.number).then(
            (response : AxiosResponse) => {

                if (response.data.numeral) {
                    newValue.numeral = response.data.numeral
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
                    <FormField name="number" label="Number">
                        <TextInput 
                            name="number"
                            type="number"
                        />
                    </FormField>
                    <Button primary type="submit" label="Convert!"/>
                </Box>
            </Form>

            {
                value.numeral && (
                    <Box>
                        <Text>{value.numeral}</Text>
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

export default NumberToRomanForm
export { NumberToRomanForm as NumberToRomanForm }