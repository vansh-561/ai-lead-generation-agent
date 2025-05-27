import streamlit as st
import time

def track_progress(graph, initial_state):
    """Track and display progress of the lead generation process"""
    progress_bar = st.progress(0)
    status_container = st.container()
    step_count = 0
    total_steps = 5
    
    try:
        with status_container:
            for step_output_dict in graph.stream(initial_state):
                step_count += 1
                progress_value = min(step_count / total_steps, 1.0)
                progress_bar.progress(progress_value)
                
                current_node_name = list(step_output_dict.keys())[0]
                current_state = step_output_dict[current_node_name]
                
                if 'messages' in current_state and current_state['messages']:
                    last_message_obj = current_state['messages'][-1]
                    if hasattr(last_message_obj, 'content'):
                        st.success(f"✅ {current_node_name}: {last_message_obj.content}")
                    elif isinstance(last_message_obj, str):
                        st.success(f"✅ {current_node_name}: {last_message_obj}")
                
                time.sleep(0.5)
        
        st.balloons()
        st.success("🎉 Enhanced lead generation completed successfully!")
        
    except Exception as e:
        st.error(f"❌ Error during execution: {str(e)}")
