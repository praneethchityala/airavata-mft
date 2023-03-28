/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.airavata.mft.controller;

import org.apache.airavata.mft.admin.MFTConsulClient;
import org.apache.airavata.mft.resource.client.StorageServiceClient;
import org.apache.airavata.mft.resource.client.StorageServiceClientBuilder;
import org.apache.airavata.mft.secret.client.SecretServiceClient;
import org.apache.airavata.mft.secret.client.SecretServiceClientBuilder;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration("ControllerConfig")
public class AppConfig {

    @org.springframework.beans.factory.annotation.Value("${consul.host}")
    String consulHost;

    @org.springframework.beans.factory.annotation.Value("${consul.port}")
    Integer consulPort;

    @org.springframework.beans.factory.annotation.Value("${resource.service.host}")
    private String resourceServiceHost;

    @org.springframework.beans.factory.annotation.Value("${resource.service.port}")
    private int resourceServicePort;

    @org.springframework.beans.factory.annotation.Value("${secret.service.host}")
    private String secretServiceHost;

    @org.springframework.beans.factory.annotation.Value("${secret.service.port}")
    private int secretServicePort;
    @Bean
    public StorageServiceClient storageServiceClient() {
        return StorageServiceClientBuilder.buildClient(resourceServiceHost, resourceServicePort);
    }

    @Bean
    public SecretServiceClient secretServiceClient() {
        return SecretServiceClientBuilder.buildClient(secretServiceHost, secretServicePort);
    }

    @Bean
    public RequestBuilder requestBuilder() {
        return new RequestBuilder();
    }

    @Bean
    public MFTConsulClient mftConsulClient() {
        return new MFTConsulClient(consulHost, consulPort);
    }

    @Bean
    public TransferDispatcher pathOptimizer() {
        TransferDispatcher agentTransferDispatcher = new TransferDispatcher();
        agentTransferDispatcher.init();
        return agentTransferDispatcher;
    }
}
