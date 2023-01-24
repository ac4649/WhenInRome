import { Box, Text } from "grommet"
import react from "react"

// We deal with converting the underscores to overlines here
interface IShowUpperBars {
    title ? : string,
    border ? : any,
    bold_title ? : boolean
    value: string
}

const ShowUpperBars = ( props : IShowUpperBars) => {
    let hasUpperBar = false
    return (
        <Box border={ props.border } pad="small" gap="small">
            {
                props.bold_title ? (
                    <Text weight="bold">{ props.title ? props.title : "Viniculum Notation Preview:" }</Text>
                ) : (
                    <Text>{ props.title ? props.title : "Viniculum Notation Preview:" }</Text>
                )
            }
            <Box direction="row">
                {
                    props.value.split("").map(
                        (cur_value, index) => {
                            if (cur_value == "_") {
                                hasUpperBar = true
                                return null
                            }

                            if (hasUpperBar) {
                                hasUpperBar = false
                                return (
                                    <Text key={index} style={{textDecoration: "overline"}}>
                                        {cur_value}
                                    </Text>
                                )
                            } else {
                                return (
                                    <Text key={index}>
                                        {cur_value}
                                    </Text>
                                )
                            } 
                    
                        }
                    )
                }
            </Box>
        </Box>
    )

}

export default ShowUpperBars
export { ShowUpperBars as ShowUpperBars}