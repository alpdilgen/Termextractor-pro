"""
Results page for TermExtractor-Pro
"""

import streamlit as st
import pandas as pd
from io import BytesIO


def show_results_page(result):
    """Show results page"""
    
    if not result or not result.terms:
        st.warning("No terms to display")
        return
    
    # Header with statistics
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Total Terms", len(result.terms))
    
    with col2:
        high_rel = len(result.get_high_relevance_terms(80))
        st.metric("High Relevance (80+)", high_rel)
    
    with col3:
        medium_rel = len(result.get_high_relevance_terms(60)) - high_rel
        st.metric("Medium Relevance (60-79)", medium_rel)
    
    with col4:
        if result.lookup_statistics:
            exact_matches = result.lookup_statistics.get('exact_matches_found', 0)
            st.metric("Bilingual Matches", exact_matches)
    
    with col5:
        if result.derivative_statistics:
            derivatives = result.derivative_statistics.get('derivatives_found', 0)
            st.metric("Derivatives Found", derivatives)
    
    st.markdown("---")
    
    # Tabs for different views
    tab_table, tab_stats, tab_export = st.tabs(["📋 Terms Table", "📊 Statistics", "💾 Export"])
    
    with tab_table:
        st.subheader("Extracted Terms")
        
        # Filters
        col1, col2, col3 = st.columns(3)
        
        with col1:
            search_term = st.text_input("Search terms", help="Filter by term text")
        
        with col2:
            min_relevance = st.slider("Min Relevance", 0, 100, 0)
        
        with col3:
            translation_source_filter = st.multiselect(
                "Translation Source",
                options=["API", "EXACT_MATCH", "FUZZY_REFERENCE"],
                default=["API", "EXACT_MATCH", "FUZZY_REFERENCE"],
            )
        
        # Prepare table data
        table_data = []
        for term in result.terms:
            if term.relevance_score < min_relevance:
                continue
            
            if search_term and search_term.lower() not in term.term.lower():
                continue
            
            if term.translation_source not in translation_source_filter:
                continue
            
            table_data.append({
                'Term': term.term,
                'Translation': term.translation or '—',
                'Source': term.translation_source,
                'Domain': term.domain,
                'POS': term.pos,
                'Relevance': f"{term.relevance_score:.1f}",
                'Confidence': f"{term.confidence_score:.1f}",
                'Freq': term.frequency,
                'Variants': len(term.variants or []),
            })
        
        # Display table
        if table_data:
            df = pd.DataFrame(table_data)
            
            # Color coding based on relevance
            def color_relevance(val):
                try:
                    score = float(val)
                    if score >= 80:
                        return 'background-color: #90EE90'  # Light green
                    elif score >= 60:
                        return 'background-color: #FFD700'  # Gold
                    else:
                        return 'background-color: #FFB6C6'  # Light pink
                except:
                    return ''
            
            styled_df = df.style.applymap(color_relevance, subset=['Relevance'])
            st.dataframe(styled_df, use_container_width=True)
            
            st.caption(f"Showing {len(table_data)} of {len(result.terms)} terms")
        else:
            st.info("No terms match the selected filters")
        
        # Show derivatives if discovered
        if any(term.discovered_derivatives for term in result.terms):
            st.markdown("---")
            st.subheader("🔬 Discovered Derivatives")
            
            derivatives_list = []
            for term in result.terms:
                if term.discovered_derivatives:
                    derivatives_list.append({
                        'Base Term': term.term,
                        'Derivative Count': len(term.discovered_derivatives),
                        'Variants': ', '.join(term.discovered_derivatives[:5]) + (
                            f"... (+{len(term.discovered_derivatives) - 5})"
                            if len(term.discovered_derivatives) > 5 else ""
                        )
                    })
            
            if derivatives_list:
                deriv_df = pd.DataFrame(derivatives_list)
                st.dataframe(deriv_df, use_container_width=True)
    
    with tab_stats:
        st.subheader("Extraction Statistics")
        
        # Main statistics
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("#### Basic Statistics")
            if result.statistics:
                for key, value in result.statistics.items():
                    st.write(f"- **{key.replace('_', ' ').title()}**: {value}")
        
        with col2:
            st.write("#### Domain Distribution")
            domain_counts = {}
            for term in result.terms:
                domain_counts[term.domain] = domain_counts.get(term.domain, 0) + 1
            
            if domain_counts:
                domain_df = pd.DataFrame({
                    'Domain': list(domain_counts.keys()),
                    'Count': list(domain_counts.values()),
                })
                st.dataframe(domain_df, use_container_width=True)
        
        # Bilingual lookup stats
        if result.lookup_statistics:
            st.markdown("---")
            st.write("#### Bilingual Lookup Statistics")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Processed", result.lookup_statistics.get('total_terms_processed', 0))
            with col2:
                st.metric("Exact Matches", result.lookup_statistics.get('exact_matches_found', 0))
            with col3:
                st.metric("Fuzzy Matches", result.lookup_statistics.get('fuzzy_matches_used', 0))
            with col4:
                lookup_rate = result.lookup_statistics.get('lookup_rate', 0)
                st.metric("Lookup Rate", f"{lookup_rate:.1f}%")
        
        # Derivative discovery stats
        if result.derivative_statistics:
            st.markdown("---")
            st.write("#### Derivative Discovery Statistics")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Single-word Terms", result.derivative_statistics.get('single_word_terms', 0))
            with col2:
                st.metric("Derivatives Found", result.derivative_statistics.get('derivatives_found', 0))
            with col3:
                avg_deriv = result.derivative_statistics.get('avg_derivatives_per_term', 0)
                st.metric("Avg per Term", f"{avg_deriv:.2f}")
            with col4:
                modes = result.derivative_statistics.get('modes_used', [])
                st.metric("Modes Used", ', '.join(modes) if modes else 'None')
    
    with tab_export:
        st.subheader("Export Results")
        
        export_format = st.selectbox(
            "Export Format",
            options=["xlsx", "csv", "json", "tbx"],
            help="Choose format for download"
        )
        
        st.info(
            "**Export information:**\n\n"
            "- **XLSX**: Spreadsheet with multiple sheets (terms, derivatives, statistics)\n"
            "- **CSV**: Comma-separated values for spreadsheets\n"
            "- **JSON**: Structured data for APIs and processing\n"
            "- **TBX**: Terminology Exchange format for CAT tools"
        )
        
        if st.button("📥 Generate Download", use_container_width=True, type="primary"):
            try:
                from src.io import FormatExporter
                
                exporter = FormatExporter()
                exported_data = exporter.export(result, export_format)
                
                # Prepare filename
                filename = f"terms_extraction.{export_format}"
                
                # Create download button
                st.download_button(
                    label=f"💾 Download {export_format.upper()}",
                    data=exported_data,
                    file_name=filename,
                    mime=_get_mime_type(export_format),
                    use_container_width=True,
                )
                
                st.success(f"✅ Ready to download {export_format.upper()}")
            
            except Exception as e:
                st.error(f"❌ Error generating export: {str(e)}")


def _get_mime_type(format_str: str) -> str:
    """Get MIME type for format"""
    mime_types = {
        'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'csv': 'text/csv',
        'json': 'application/json',
        'tbx': 'application/xml',
    }
    return mime_types.get(format_str, 'application/octet-stream')
