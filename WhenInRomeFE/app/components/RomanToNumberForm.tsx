import { AxiosResponse } from "axios";
import { Box, BoxProps, Button, Form, FormExtendedEvent, FormField, Text, TextInput } from "grommet"
import React from "react"
const axios = require('axios');

interface IRomanToNumberForm {
    formTitle: string
    formBoxProps : BoxProps
}

interface IFormValue {
    numeral: string
    number ? : number
    error ? : string
}

const RomanToNumberForm = ( props : IRomanToNumberForm ) => {

    const [value, setValue] = React.useState<IFormValue>({numeral: ""})

    const onSubmit = ( event: FormExtendedEvent<IFormValue, Element> ) => {
        let newValue : IFormValue = {
            numeral : event.value.numeral
        }
        axios.get("/api/numeralToNumber?numeral=" + event.value.numeral).then(
            (response : AxiosResponse) => {

                if (response.data.number) {
                    newValue.number = response.data.number
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
                    <FormField name="numeral" label="Roman Numeral">
                        <TextInput 
                            name="numeral"
                        />
                    </FormField>
                    <Button primary type="submit" label="Convert!"/>
                </Box>
            </Form>

            {
                value.number && (
                    <Box>
                        <Text>{value.number}</Text>
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

export default RomanToNumberForm
export { RomanToNumberForm as RomanToNumberForm }